id_array=(1 2 3)
type_array=(key text)
item_array=(E D)
for id in ${id_array[@]}
do
    for type in ${type_array[@]}
    do 
            for item in ${item_array[@]}
            do 
            touch "${id}_${item}_${type}.txt"
            done
    done
done