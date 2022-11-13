<?php
// Algoritmo em PHP que mostra a soma dos números pares entre 1 e 50

$soma = 0;

for ($num = 1; $num <= 50; $num++) {
    if ($num % 2 == 0) {
        $soma += $num;
    }
}

echo "Soma = " . $soma;