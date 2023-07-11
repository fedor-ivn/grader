while read -p "> " command; do
    case $command in
        help)
            echo "Доступные команды:"
            # echo
            echo "  help         - вывести справку по командам"
            echo "  add-review   - добавить отзыв"
            echo "  list-reviews - показать все отзывы"
            echo "  clear        - удалить все отзывы"
            ;;

        add-review)
            read -p "Введите свой отзыв: " review
            if [[ $REVIEWS == "" ]]; then
                REVIEWS="-----
$review
-----"
            else
                REVIEWS="$REVIEWS
$review
-----"
            fi
            echo "Спасибо за ваш отзыв!"
            ;;

        list-reviews)
            if [[ $REVIEWS == "" ]]; then
                echo "Отзывов ещё нет :("
            else
                echo "$REVIEWS"
            fi
            ;;

        clear)
            REVIEWS=""
            echo "Все отзывы удалены"
            ;;

        "") continue ;;
        *)
            echo "Неизвестная команда. Введите help, чтобы узнать о доступных командах"
            ;;
    esac
done
