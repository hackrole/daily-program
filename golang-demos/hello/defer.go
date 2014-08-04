package main

import "fmt"

func main1() {
	defer fmt.Printf("\n")
	for i := 0; i < 5; i++ {
		defer fmt.Printf("%d ", i)
	}
}
