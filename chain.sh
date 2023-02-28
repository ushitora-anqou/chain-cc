#!/usr/bin/bash -xeu

do_case(){
    compilers=( "$@" )
    root=$PWD

    workdir="$root/build/case"
    for c in ${compilers[@]}; do
        workdir="$workdir-$c"
    done
    rm -rf $workdir
    mkdir $workdir

    current_compiler=""
    current_compiler_workdir=""
    for i in "${!compilers[@]}"; do
        target="${compilers[$i]}"

        echo ">>>>> Prepare $target"
        target_workdir=$workdir/$i-$target
        rsync -av script/$target/ $target_workdir/
        pushd $target_workdir
        ./prepare $current_compiler_workdir/compile
        popd

        current_compiler=$target
        current_compiler_workdir=$target_workdir
    done

    echo ">>>>> Test $current_compiler"
    cd $current_compiler_workdir
    SCRIPT=compile python ../../../testsuite/test_correctly_accepts.py

    #rsync -av script/$target/ $workdir/target/
    #rsync -av script/$compiler/ $workdir/compiler/

    ## Prepare the compiler (backed by gcc)
    #pushd $workdir/compiler
    #./prepare $root/script/gcc/compile
    #popd

    ## Prepare the target & perform the testsuite
    #cd $workdir/target
    #./prepare $workdir/compiler/compile
    #SCRIPT=compile python ../../../testsuite/test_correctly_accepts.py
}

mkdir -p build
do_case "$@"
