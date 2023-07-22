sample=$RANDOM

if [[ $sample -lt 8192 ]]; then
    echo "Красная"
elif [[ $sample -lt 16384 ]]; then
    echo "Жёлтая"
elif [[ $sample -lt 24576 ]]; then
    echo "Зелёная"
else
    echo "Синяя"
fi
