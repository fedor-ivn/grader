#!/bin/sh

read -p "Подпись к мему: " caption
read -p "Название файла: " output_file
convert $TEMPLATE_FILE -gravity south -annotate 0 "$caption" $output_file
echo "Мем сохранён!"
