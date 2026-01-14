#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')


    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set format of output'
    )
    args = parser.parse_args()
    
    # Для первого шага просто выводим имена файлов
    print(f"Comparing {args.first_file} and {args.second_file}")
    print(f"Output format: {args.format}")

if __name__ == '__main__':
    main()
