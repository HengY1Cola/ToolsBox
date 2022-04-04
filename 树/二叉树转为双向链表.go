package main

import (
	"fmt"
	"github.com/isdamir/gotype"
	"sort"
)

var (
	pHead *gotype.BNode
	pEnd  *gotype.BNode
)

func Array2TreeCopy(array []int, start int, end int) *gotype.BNode {
	var rootNode *gotype.BNode
	if end >= start {
		rootNode = gotype.NewBNode()
		mid := (start + end + 1) / 2
		rootNode.Data = array[mid]
		rootNode.RightChild = Array2TreeCopy(array, mid+1, end)
		rootNode.LeftChild = Array2TreeCopy(array, start, mid-1)
	}
	return rootNode
}

func BTree2Sheet(root *gotype.BNode) {
	if root == nil {
		return
	}
	BTree2Sheet(root.LeftChild)
	root.LeftChild = pEnd
	if pEnd == nil {
		pHead = root
	} else {
		pEnd.RightChild = root
	}
	pEnd = root
	BTree2Sheet(root.RightChild)
}

func main() {
	intArray := []int{1, 3, 4, 5, 8, 2, 3, 6, 4, 7}
	sort.Ints(intArray)
	root := Array2TreeCopy(intArray, 0, len(intArray)-1)
	BTree2Sheet(root)
	fmt.Println("正序")
	for pHead != nil {
		fmt.Printf("%v ", pHead.Data)
		pHead = pHead.RightChild
	}
	fmt.Println("")
	fmt.Println("倒序")
	for pEnd != nil {
		fmt.Printf("%v ", pEnd.Data)
		pEnd = pEnd.LeftChild
	}
}
