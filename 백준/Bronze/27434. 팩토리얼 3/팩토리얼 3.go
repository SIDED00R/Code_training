package main

import (
	"fmt"
	"math/big"
)

func main() {
	var n int
	fmt.Scan(&n)

	factorial := big.NewInt(1)

	for i := 2; i <= n; i++ {
		factorial.Mul(factorial, big.NewInt(int64(i)))
	}

	fmt.Println(factorial)
}
