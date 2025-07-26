#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from pathlib import Path
from difflib import unified_diff
import argparse

class MarkdownTranslationComparer:
    def __init__(self, ru_dir="docs/ru", est_dir="docs/est"):
        self.ru_dir = Path(ru_dir)
        self.est_dir = Path(est_dir)
        
    def extract_content_blocks(self, file_path):
        """Извлекает блоки контента из markdown файла"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            return None, None
            
        # Разделяем front matter и контент
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front_matter = parts[1].strip()
            main_content = parts[2].strip()
        else:
            front_matter = ""
            main_content = content.strip()
            
        # Разбиваем контент на абзацы (по двойным переносам)
        paragraphs = [p.strip() for p in main_content.split('\n\n') if p.strip()]
        
        return front_matter, paragraphs
    
    def clean_markdown(self, text):
        """Очищает markdown разметку для сравнения структуры"""
        # Убираем markdown разметку, но сохраняем структуру
        text = re.sub(r'^\s*#+\s*', '', text, flags=re.MULTILINE)  # заголовки
        text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # жирный текст
        text = re.sub(r'\*(.*?)\*', r'\1', text)  # курсив
        text = re.sub(r'`(.*?)`', r'\1', text)  # код
        text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)  # ссылки
        return text.strip()
    
    def show_processed_content(self, filename, show_raw=False, show_paragraphs=False, show_cleaned=False):
        """Показывает как выглядит обработанный контент"""
        ru_file = self.ru_dir / filename
        est_file = self.est_dir / filename
        
        print(f"\n{'='*60}")
        print(f"ОТЛАДКА: Обработанный контент для {filename}")
        print(f"{'='*60}")
        
        for lang, file_path in [("RU", ru_file), ("EST", est_file)]:
            if not file_path.exists():
                print(f"❌ {lang} файл не найден: {file_path}")
                continue
                
            print(f"\n🔍 {lang} файл: {file_path}")
            
            # Показываем сырой контент
            if show_raw:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        raw_content = f.read()
                    print(f"\n📄 СЫРОЙ КОНТЕНТ ({lang}):")
                    print("─" * 40)
                    print(repr(raw_content))  # repr показывает все символы включая \n
                    print("─" * 40)
                except Exception as e:
                    print(f"❌ Ошибка чтения: {e}")
                    continue
            
            # Извлекаем front matter и абзацы
            front_matter, paragraphs = self.extract_content_blocks(file_path)
            
            if paragraphs is None:
                print(f"❌ Не удалось обработать {lang} файл")
                continue
            
            print(f"\n📋 FRONT MATTER ({lang}):")
            print("─" * 40)
            print(repr(front_matter))
            print("─" * 40)
            
            if show_paragraphs:
                print(f"\n📝 АБЗАЦЫ ПОСЛЕ РАЗБИВКИ ({lang}) - {len(paragraphs)} шт.:")
                for i, para in enumerate(paragraphs, 1):
                    print(f"\n[Абзац {i}] ({len(para)} символов):")
                    print("─" * 30)
                    print(repr(para))  # показываем все символы
                    print("─" * 30)
                    print("Как выглядит:")
                    print(para)
                    
                    if show_cleaned:
                        cleaned = self.clean_markdown(para)
                        print("После очистки markdown:")
                        print(repr(cleaned))
                        print("Очищенный вид:")
                        print(cleaned)
                    print()

    def compare_files(self, filename):
        """Сравнивает русский и эстонский файлы"""
        ru_file = self.ru_dir / filename
        est_file = self.est_dir / filename
        
        print(f"\n{'='*60}")
        print(f"Сравнение файла: {filename}")
        print(f"{'='*60}")
        
        # Проверяем существование файлов
        if not ru_file.exists():
            print(f"❌ Русский файл не найден: {ru_file}")
            return
        if not est_file.exists():
            print(f"❌ Эстонский файл не найден: {est_file}")
            return
            
        # Извлекаем контент
        ru_front, ru_paragraphs = self.extract_content_blocks(ru_file)
        est_front, est_paragraphs = self.extract_content_blocks(est_file)
        
        if ru_paragraphs is None or est_paragraphs is None:
            print("❌ Ошибка при чтении файлов")
            return
            
        # Сравниваем количество абзацев
        print(f"📊 Статистика:")
        print(f"   Русский: {len(ru_paragraphs)} абзацев")
        print(f"   Эстонский: {len(est_paragraphs)} абзацев")
        
        if len(ru_paragraphs) != len(est_paragraphs):
            print(f"⚠️  ВНИМАНИЕ: Разное количество абзацев!")
        
        # Сравниваем front matter
        if ru_front != est_front:
            print(f"\n📝 Front Matter отличается:")
            self.show_diff("RU Front Matter", "EST Front Matter", ru_front, est_front)
        
        # Сравниваем абзацы
        max_paragraphs = max(len(ru_paragraphs), len(est_paragraphs))
        
        missing_translations = []
        structural_differences = []
        
        for i in range(max_paragraphs):
            print(f"\n--- Абзац {i+1} ---")
            
            ru_para = ru_paragraphs[i] if i < len(ru_paragraphs) else "[ОТСУТСТВУЕТ]"
            est_para = est_paragraphs[i] if i < len(est_paragraphs) else "[PUUDUB]"
            
            if ru_para == "[ОТСУТСТВУЕТ]":
                print("❌ Русский абзац отсутствует")
                missing_translations.append(f"Абзац {i+1}: отсутствует русский")
            elif est_para == "[PUUDUB]":
                print("❌ Эстонский абзац отсутствует")
                missing_translations.append(f"Абзац {i+1}: отсутствует эстонский")
            else:
                # Проверяем структурное соответствие
                ru_clean = self.clean_markdown(ru_para)
                est_clean = self.clean_markdown(est_para)
                
                # Простая эвристика: проверяем длину и количество предложений
                ru_sentences = len([s for s in ru_clean.split('.') if s.strip()])
                est_sentences = len([s for s in est_clean.split('.') if s.strip()])
                
                if abs(ru_sentences - est_sentences) > 1:
                    structural_differences.append(f"Абзац {i+1}: RU={ru_sentences} предл., EST={est_sentences} предл.")
                
                # Показываем содержимое абзацев
                print(f"🇷🇺 RU ({len(ru_para)} симв.): {ru_para[:100]}{'...' if len(ru_para) > 100 else ''}")
                print(f"🇪🇪 EST ({len(est_para)} симв.): {est_para[:100]}{'...' if len(est_para) > 100 else ''}")
                
                if structural_differences and structural_differences[-1].startswith(f"Абзац {i+1}"):
                    print(f"⚠️  Возможно структурное различие: {structural_differences[-1]}")
        
        # Итоговый отчет
        print(f"\n{'='*40}")
        print("📋 ИТОГОВЫЙ ОТЧЕТ:")
        print(f"{'='*40}")
        
        if not missing_translations and not structural_differences:
            print("✅ Файлы структурно соответствуют друг другу")
        else:
            if missing_translations:
                print("❌ Отсутствующие переводы:")
                for item in missing_translations:
                    print(f"   • {item}")
            
            if structural_differences:
                print("⚠️  Структурные различия:")
                for item in structural_differences:
                    print(f"   • {item}")
    
    def show_diff(self, label1, label2, text1, text2):
        """Показывает diff между двумя текстами"""
        diff = unified_diff(
            text1.splitlines(keepends=True),
            text2.splitlines(keepends=True),
            fromfile=label1,
            tofile=label2,
            n=3
        )
        
        for line in diff:
            if line.startswith('+++') or line.startswith('---'):
                print(f"📄 {line.strip()}")
            elif line.startswith('@@'):
                print(f"📍 {line.strip()}")
            elif line.startswith('+'):
                print(f"🟢 {line.rstrip()}")
            elif line.startswith('-'):
                print(f"🔴 {line.rstrip()}")
            else:
                print(f"   {line.rstrip()}")
    
    def find_all_markdown_files(self):
        """Находит все markdown файлы для сравнения"""
        ru_files = set()
        est_files = set()
        
        if self.ru_dir.exists():
            ru_files = {f.name for f in self.ru_dir.glob("*.md")}
        
        if self.est_dir.exists():
            est_files = {f.name for f in self.est_dir.glob("*.md")}
        
        all_files = ru_files.union(est_files)
        return sorted(all_files)
    
    def compare_all_files(self):
        """Сравнивает все найденные markdown файлы"""
        files = self.find_all_markdown_files()
        
        if not files:
            print("❌ Markdown файлы не найдены в указанных директориях")
            return
        
        print(f"🔍 Найдено {len(files)} файлов для сравнения")
        
        for filename in files:
            self.compare_files(filename)
            
        print(f"\n{'='*60}")
        print("✅ Сравнение завершено!")
        print(f"{'='*60}")

def main():
    parser = argparse.ArgumentParser(description="Сравнение переводов Jekyll сайта (русский-эстонский)")
    parser.add_argument("--ru-dir", default="docs/ru", help="Директория с русскими файлами")
    parser.add_argument("--est-dir", default="docs/est", help="Директория с эстонскими файлами")
    parser.add_argument("--file", help="Конкретный файл для сравнения (например: exhaustion.md)")
    
    # Опции отладки
    parser.add_argument("--debug", action="store_true", help="Показать отладочную информацию")
    parser.add_argument("--show-raw", action="store_true", help="Показать сырой контент файлов")
    parser.add_argument("--show-paragraphs", action="store_true", help="Показать разбивку на абзацы")
    parser.add_argument("--show-cleaned", action="store_true", help="Показать очищенный от markdown текст")
    
    args = parser.parse_args()
    
    comparer = MarkdownTranslationComparer(args.ru_dir, args.est_dir)
    
    if args.debug and args.file:
        # Режим отладки - показываем как обрабатывается файл
        comparer.show_processed_content(
            args.file, 
            show_raw=args.show_raw,
            show_paragraphs=args.show_paragraphs or True,  # по умолчанию показываем абзацы в debug
            show_cleaned=args.show_cleaned
        )
    elif args.file:
        comparer.compare_files(args.file)
    else:
        comparer.compare_all_files()

if __name__ == "__main__":
    main()