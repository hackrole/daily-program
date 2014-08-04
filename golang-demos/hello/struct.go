package main

import "fmt"

type person struct {
	name string
	age  int
}

func Older(p1, p2 person) (person, int) {
	if p1.age > p2.age {
		return p1, p1.age - p2.age
	}
	return p2, p2.age - p1.age
}

func main5() {
	var tom person

	tom.name, tom.age = "Tom", 18

	bob := person{age: 25, name: "bob"}

	paul := person{"paul", 43}

	tb_older, tb_diff := Older(tom, bob)
	tp_older, tp_diff := Older(tom, paul)
	bp_older, bp_diff := Older(bob, paul)

	fmt.Printf("of %s and %s, %s is older by %d year\n",
		tom.name, bob.name, tb_older.name, tb_diff)

	fmt.Printf("of %s and %s, %s is older by %d year\n",
		tom.name, bob.name, tp_older.name, tp_diff)

	fmt.Printf("of %s and %s, %s is older by %d year\n",
		bob.name, bob.name, bp_older.name, bp_diff)
}
