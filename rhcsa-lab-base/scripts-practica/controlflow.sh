if [ $base -eq 1 ] && [ $dm -eq 1 ]; then
    installDMBase
elif [ $base -ne 1 ] && [ $dm -eq 1]; then
    installBase
elif[ $base -ne1 ] && [ $dm -eq 1]; then
    installDM
else
    echo '==> Installing nothing'
fi

