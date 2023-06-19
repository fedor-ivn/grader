# read -p "Подпись к мему: " caption
# read -p "Название файла: " output_file
TEMPLATE_FILE="template.jpg"
caption="Подпись к мему"
output_file="meme.jpg"
convert $TEMPLATE_FILE -gravity south -annotate 0 "$caption" $output_file
echo "Мем сохранён!"
