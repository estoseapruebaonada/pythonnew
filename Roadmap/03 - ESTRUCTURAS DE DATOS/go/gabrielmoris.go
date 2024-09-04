/*
 * EXERCISE:
 * - Show examples of creating all the structures supported by default
 *   in your language.
 * - Use operations of insertion, deletion, updating, and sorting.
 *
 * EXTRA DIFFICULTY (optional):
 * Create a contact book via terminal.
 * - You must implement functionalities for searching, inserting, updating,
 *   and deleting contacts.
 * - Each contact must have a name and a phone number.
 * - The program first asks what operation you want to perform,
 *   and then the necessary data to carry it out.
 * - The program cannot allow the input of non-numeric phone numbers and with more
 *   than 11 digits (or the number of digits you want).
 * - An operation to end the program should also be proposed.
 */

package main

import (
	"fmt"
	"sync"
)

func main(){
	dataStructures()
	challenge()
}

func dataStructures() {
    fmt.Println("Array: Fixed size of elements of the same type")
    var arr [5]int
    fmt.Println(arr)

    fmt.Println("Slices: Dynamic resizable Arrays of the same type")
    slice := []int{1, 2, 3, 4}
    fmt.Println(slice)

    fmt.Println("Maps: Implementation of hash tables / dictionaries")
    m := map[string]int{"apple": 1, "banana": 2}
    fmt.Println(m)

    fmt.Println("Structs: User-defined types that groups variables of different types")
    type Person struct {
        name string
        age  int
    }
    p := Person{
        name: "pepe",
        age:  45,
    }
    fmt.Println(p)

    fmt.Println("Pointers: Holds the memory address of a value")
    var point *int = &p.age
    fmt.Println(point)

    fmt.Println("Interface: Define a set of method signatures")
    type Animal interface {
        Feed()
        Play()
    }
	// Use of the Interface outside this function.
	d.Feed()

	fmt.Println("Channels: Used for communication between go routines")
	ch := make(chan int)

    var wg sync.WaitGroup
    wg.Add(2) // We're waiting for 2 goroutines

    go sender(ch, &wg)
    go receiver(ch, &wg)

    wg.Wait() // Wait for both goroutines to finish
}

// U se of the interface Animal
type Dog struct {
	name string
}
var d = Dog{
	name: "pepe",
}
func (d Dog) Feed() { // Implementing Feed method for Dog
	fmt.Println(d.name, "is eating dog food.")
}


// Brief Explanation about Channels
// A goroutine is a lightweight thread of execution that runs concurrently within a Go program.
// Channels are a type-safe mechanism for communicating between goroutines. 

func sender(ch chan int, wg *sync.WaitGroup) {
    defer wg.Done() // Signal that this goroutine is done when the function returns
    for i := 0; i < 5; i++ {
        ch <- i
    }
    close(ch)
}

func receiver(ch chan int, wg *sync.WaitGroup) {
    defer wg.Done() // Signal that this goroutine is done when the function returns
    for {
        value, ok := <-ch
        if !ok {
            fmt.Println("Channel closed")
            break
        }
        fmt.Println("Received:", value)
    }
}

////////////////////// CHALLENGE //////////////////////

func challenge(){

}