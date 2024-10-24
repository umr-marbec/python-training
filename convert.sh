for dir in blocks data_types introduction io oop plots maps
do
    cd $dir
    for f in *py
    do
        echo $f
        if [ $f = "pyngl.py" ]; then
            echo "============================== PyNGL not processed"
            continue
        fi

        # Convert .py to ipynb
        jupytext --to notebook $f
        fout=`echo $f | sed "s/.py/.ipynb/"`

        # execute notebooks
        jupyter nbconvert --execute --to notebook $fout

        final_file=`echo $fout | sed "s/ipynb/nbconvert.ipynb/"`
        mv $final_file $fout

    done
    cd ..
done

cd misc
for f in nemo.py eof_analysis.py interpol.py practical_session.py shapefiles.py
do

    echo $f

    # Convert .py to ipynb
    jupytext --to notebook $f
    fout=`echo $f | sed "s/.py/.ipynb/"`

    # execute notebooks
    jupyter nbconvert --execute --to notebook $fout

    final_file=`echo $fout | sed "s/ipynb/nbconvert.ipynb/"`
    mv $final_file $fout
done

for f in dask_covariance.py dask_examples.py mean_sst_dask.py
do
    echo $f
    # Convert .py to ipynb
    jupytext --to notebook $f
done

cd ..
