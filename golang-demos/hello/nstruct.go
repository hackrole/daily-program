package main

import "fmt"

type Human struct {
	name   string
	age    int
	weight int
}

type Student struct {
	Human // 匿名字段, == include
	spe   string
}

func main6() {
	mark := Student{Human{"mark", 25, 120}, "Compute scs"}

	fmt.Println("His name is ", mark.name)
	fmt.Println("his age is ", mark.age)
	fmt.Println("his weight is ", mark.weight)
	fmt.Println("his spe is ", mark.spe)

	mark.spe = "AI"
	fmt.Println("mark changed his spe")
	fmt.Println("his spe is ", mark.spe)
	fmt.Println("mark become old")
	mark.age = 46
	fmt.Println("his age is ", mark.age)
	fmt.Println("he become more weight")
	mark.weight += 60
	fmt.Println("his weight is ", mark.weight)
}
