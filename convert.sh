for dir in blocks data_types introduction io oop plots maps
do
    cd $dir
    for f in *py
    do
        echo $f

        # Convert .py to ipynb
        jupytext --to notebook $f
        fout=`echo $f | sed "s/.py/.ipynb/"`

        # execute notebooks
        jupyter nbconvert --execute --to notebook $fout
    done
    cd ..
done

