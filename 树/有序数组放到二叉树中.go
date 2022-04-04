package main

import (
	"github.com/isdamir/gotype"
	"sort"
)

func array2Tree(array []int, start int, end int) *gotype.BNode {
	var rootNode *gotype.BNode
	if end >= start {
		rootNode = gotype.NewBNode()
		mid := (start + end + 1) / 2
		rootNode.Data = array[mid]
		rootNode.RightChild = array2Tree(array, mid+1, end)
		rootNode.LeftChild = array2Tree(array, start, mid-1)
	}
	return rootNode
}

func main() {
	intArray := []int{1, 3, 4, 5, 8, 2, 3, 6, 4, 7}
	sort.Ints(intArray)
	root := array2Tree(intArray, 0, len(intArray)-1)
	gotype.PrintTreeMidOrder(root)

}
