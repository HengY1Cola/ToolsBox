#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
typedef int SDataType;
//链表的节点
typedef struct SListNode
{
	SDataType _data;
	struct SListNode* _PNext;
}Node, * PNode;
typedef struct SList       //封装了链表的结构
{
	PNode _pHead;//指向链表第一个节点
}SList;
void SListInit(SList* s) {
	assert(s);
	s->_pHead = NULL;
}//链表初始化
struct SListNode* BuySListNode(SDataType data) {
	struct SListNode* p;
	p = (SListNode*)malloc(sizeof(struct SListNode));
	p->_data = data;
	p->_PNext = NULL;
	return p;
}
void SListPushBack(SList* s, SDataType data) {
	//找链表最后一个节点
	assert(s);
	PNode pNewNode = BuySListNode(data);
	if (s->_pHead == NULL) {//链表没有节点的情况
		s->_pHead = pNewNode;
	}
	else {
		PNode pCur = s->_pHead;
		while (pCur->_PNext) {
			pCur = pCur->_PNext;
		}
		//让最后一个节点指向新节点
		pCur->_PNext = pNewNode;
	}
}//尾插
void SListPrint(SList* s) {            
	assert(s);
	PNode pCur = s->_pHead;
	while (pCur) {
		printf("%d--->", pCur->_data);
		pCur = pCur->_PNext;
	}
	printf("\n");
} //打印链表
void SListPrint2(struct SListNode* head) {
	while (head) {
		printf("%d--->", head->_data);
		head = head->_PNext;
	}
}//没有封装输出
struct SListNode* swapPairs(struct SListNode *_pHead) {
	if (_pHead == NULL || _pHead->_PNext == NULL) return _pHead;
	struct SListNode* nex = _pHead->_PNext;
	_pHead->_PNext = swapPairs(nex->_PNext);//递归完head->next->next之后所有节点交换完毕
	nex->_PNext = _pHead;
	return nex;
}
void main() {
	SList s;
	SListInit(&s);
	SListPushBack(&s, 1);
	SListPushBack(&s, 2);
	SListPushBack(&s, 3);
	SListPushBack(&s, 4);
	SListPrint(&s);
	SListPrint2(swapPairs(s._pHead));
}