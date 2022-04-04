package main

import "fmt"

// 这道题有点巧妙呀
// 例如 A->B C->D B->C
// 那么 能够确定有4个以及确定终点在哪里
// 那么反转回来 没有出点的就是起点了 然后根据起点来走就好了

func findStart(input map[string]string) {
	// todo 调换信息
	reverse := map[string]string{}
	for k, v := range input {
		reverse[v] = k
	}
	// todo 寻找起点
	start := ""
	for k, _ := range input {
		if _, ok := reverse[k]; !ok {
			start = k
			break
		}
	}
	// todo 从起点开始串通
	if start == "" {
		fmt.Println("找不到")
		return
	} else {
		for {
			if _, ok := input[start]; !ok {
				fmt.Printf("%v", start)
				break // 到达末尾了
			} else {
				fmt.Printf("%v -> ", start)
				next := input[start]
				start = next
			}
		}
	}
}

func main() {
	input := map[string]string{
		"西安": "成都",
		"北京": "上海",
		"大连": "西安",
		"上海": "大连",
	}
	findStart(input)
}
