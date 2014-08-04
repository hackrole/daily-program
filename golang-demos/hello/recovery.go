package main

import "os"

var user = os.Getenv("USER")

func init() {
	if user == "" {
		panic("no value for $USER")
	}
}

func throwPainc(f func()) (b bool) {
	return
}
