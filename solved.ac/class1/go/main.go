// https://www.acmicpc.net/problem/10430
package main

import "fmt"

func main(){
	var a, b, c int
	fmt.Scanf("%d %d %d", &a, &b, &c)
	fmt.Println((a + b) % c)
	fmt.Println((a%c + b%c) % c)
	fmt.Println((a * b) % c)
	fmt.Println((a % c * b % c) % c)
}