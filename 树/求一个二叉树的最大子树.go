package main

import (
	"fmt"
	"github.com/isdamir/gotype"
	"math"
)

func makeOneTree() *gotype.BNode {
	root := &gotype.BNode{}
	node1 := &gotype.BNode{}
	node2 := &gotype.BNode{}
	node3 := &gotype.BNode{}
	node4 := &gotype.BNode{}
	root.Data = 6
	root.LeftChild = node1
	root.RightChild = node2
	node1.LeftChild = node3
	node1.RightChild = node4
	node1.Data = 3
	node2.Data = -7
	node3.Data = -1
	node4.Data = 9
	return root
}

var MaxNum = math.MinInt64
var MaxNode = &gotype.BNode{}

func findMaxSubTree(root *gotype.BNode) (int, *gotype.BNode) {
	if root == nil {
		return 0, root
	}
	lMax, _ := findMaxSubTree(root.LeftChild)
	rMax, _ := findMaxSubTree(root.RightChild)
	sum := root.Data.(int) + lMax + rMax
	fmt.Printf("当前的节点：%v, sum: %v lMax: %v, rMax: %v\n", root.Data, sum, lMax, rMax)
	if sum > MaxNum {
		MaxNum = sum
		MaxNode = root
	}
	return sum, MaxNode

}
func main() {
	root := makeOneTree()
	resNum, resNode := findMaxSubTree(root)
	fmt.Println(resNum)
	fmt.Println(resNode.Data)
}
