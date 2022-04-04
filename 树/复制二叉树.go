package main

import (
	"fmt"
	"github.com/isdamir/gotype"
	"sort"
)

func Array2TreeCopy2(array []int, start int, end int) *gotype.BNode {
	var rootNode *gotype.BNode
	if end >= start {
		rootNode = gotype.NewBNode()
		mid := (start + end + 1) / 2
		rootNode.Data = array[mid]
		rootNode.RightChild = Array2TreeCopy2(array, mid+1, end)
		rootNode.LeftChild = Array2TreeCopy2(array, start, mid-1)
	}
	return rootNode
}

func copyTree(treeRoot *gotype.BNode) *gotype.BNode {
	if treeRoot == nil {
		return nil
	}
	root := gotype.NewBNode()
	root.Data = treeRoot.Data
	root.LeftChild = copyTree(treeRoot.LeftChild)
	root.RightChild = copyTree(treeRoot.RightChild)
	return root
}

func main() {
	intArray := []int{1, 3, 4, 5, 8, 2, 3, 6, 4, 7}
	sort.Ints(intArray)
	root := Array2TreeCopy2(intArray, 0, len(intArray)-1)
	gotype.PrintTreeMidOrder(root)
	fmt.Println("")
	newRoot := copyTree(root)
	gotype.PrintTreeMidOrder(newRoot)
}
