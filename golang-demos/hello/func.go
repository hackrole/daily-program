package main

import "fmt"

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func sumAndpRoduct(a int, b int) (int, int) {
	return a + b, a * b
}

func sumP2(a, b int) (add int, mult int) {
	add = a + b
	mult = a * b
	return
}

func argSlice(arg ...int) {
	for _, n := range arg {
		fmt.Printf("the num is %d\n", n)
	}
}

func main2() {
	x := 3
	y := 4
	z := 5

	max_xy := max(x, y)
	max_xz := max(x, z)

	fmt.Printf("max(x%d, %d) = %d\n", x, y, max_xy)
	fmt.Printf("max(x%d, %d) = %d\n", y, z, max_xz)
	fmt.Printf("max(x%d, %d) = %d\n", x, z, max(x, z))
	sum, prod := sumAndpRoduct(x, y)
	fmt.Printf("sum=%d, prod=%d\n", sum, prod)
	sum, prod = sumP2(z, y)
	fmt.Printf("sum=%d, prod=%d\n", sum, prod)
	argSlice(1, 2, 3, 4)
	argSlice(1, 2, 3, 4, 5, 6)
}
