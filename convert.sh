for dir in blocks data_types introduction io misc oop plots maps
do
    cd $dir
    ls *py
    for f in *py
    do
        echo $f
        jupytext --to notebook $f
    done
    cd ..
done

