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
struct SListNode* BuySListNode(SDataType data) { 
	struct SListNode* p;
	p = (SListNode*)malloc(sizeof(struct SListNode));
	p->_data = data;
	p->_PNext = NULL;
	return p;
}
void SListInit(SList* s) {
	assert(s);
	s->_pHead = NULL;
}//链表初始化
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
void SListPopBack(SList* s) {
	assert(s);
	if (s->_pHead == NULL) {//链表中没有节点
		return;
	}
	else if (s->_pHead->_PNext == NULL) {//只有一个节点
		free(s->_pHead);
		s->_pHead = NULL;
	}
	else {                           //多个节点
		PNode pCur = s->_pHead;
		PNode pPre = NULL;
		while (pCur->_PNext) {
			pPre = pCur;
			pCur = pCur->_PNext;
		}
		free(pCur);
		pPre->_PNext = NULL;
	}
}//尾删
void SListPushFront(SList* s, SDataType data) {
	assert(s);
	PNode pNewNode = BuySListNode(data);
	if (s->_pHead == NULL) {//链表为空
		s->_pHead = pNewNode;
	}
	else {
		pNewNode->_PNext = s->_pHead;
		s->_pHead = pNewNode;
	}
}//头插
void SListPopFront(SList* s) {
	assert(s);
	if (s->_pHead == NULL) {//链表为空
		return;
	}
	else if (s->_pHead->_PNext == NULL) {//只有一个节点
		free(s->_pHead);
		s->_pHead = NULL;
	}
	else {
		PNode pCur = s->_pHead;
		s->_pHead = pCur->_PNext;
		free(pCur);
	}
}//头删
void SListInsert(PNode pos, SDataType data) {
	PNode pNewNode = NULL;
	if (pos == NULL) {
		return;
	}
	pNewNode = BuySListNode(data);

	pNewNode->_PNext = pos->_PNext;
	pos->_PNext = pNewNode;
}//插入
PNode SListFind(SList* s, SDataType data) {
	assert(s);
	PNode pCur = s->_pHead;
	while (pCur) {
		if (pCur->_data == data) {
			return pCur;
		}
		pCur = pCur->_PNext;
	}
	return NULL;
}//查找
void SListErase(SList* s, PNode pos) {
	assert(s);
	if (pos == NULL || s->_pHead == NULL) {
		return;
	}
	if (pos == s->_pHead) {
		s->_pHead = pos->_PNext;
	}
	else {
		PNode pPrePos = s->_pHead;
		while (pPrePos && pPrePos->_PNext != pos) {
			pPrePos = pPrePos->_PNext;
		}
		pPrePos->_PNext = pos->_PNext;
	}
	free(pos);
}//删除给定pos位置的节点。
void SListRemove(SList* s, SDataType data) {
	assert(s);
	if (s->_pHead == NULL) {
		return;
	}
	PNode pPre = NULL;
	PNode pCur = s->_pHead;
	while (pCur) {
		if (pCur->_data == data) {
			if (pCur == s->_pHead) {         //要删除的是第一个位置的节点
				s->_pHead = pCur->_PNext;
			}
			else {
				pPre->_PNext = pCur->_PNext;      //其它位置的情况，让前一个节点指向其后一个节点
			}
			free(pCur);
			return;
		}
		else {
			pPre = pCur;
			pCur = pCur->_PNext;
		}
	}
}//删除第一个值为data的节点
int SListSize(SList* s) {            //获取链表有效节点的个数
	assert(s);
	int count = 0;
	PNode pCur = s->_pHead;
	while (pCur) {
		count++;
		pCur = pCur->_PNext;
	}
	return count;
}
int SListEmpty(SList* s) {              //检测链表是否为空
	assert(s);
	if (s->_pHead == NULL) {
		return -1;
	}
	return 0;
}
void SListClear(SList* s) {             //清空链表
	assert(s);
	if (s->_pHead == NULL) {
		return;
	}
	PNode pCur = s->_pHead;
	while (pCur->_PNext) {    //循环清空链表中的节点
		PNode Tmp = pCur->_PNext;
		free(pCur);
		pCur = Tmp;
	}
	if (pCur) {      //清空最后一个节点
		free(pCur);
		pCur = NULL;
	}
}
void SListDestroy(SList* s) {            //销毁链表
	assert(s);
	if (s->_pHead == NULL) {
		free(s->_pHead);
		return;
	}
	while (s->_pHead) {
		PNode Tmp = s->_pHead->_PNext;
		free(s->_pHead);
		s->_pHead = Tmp;
	}
}
void SListPrint(SList* s) {             //打印链表
	assert(s);
	PNode pCur = s->_pHead;
	while (pCur) {
		printf("%d--->", pCur->_data);
		pCur = pCur->_PNext;
	}
	printf("\n");
}
struct SListNode* rotateRight(struct SListNode* _pHead, int k) {
	if (_pHead == NULL || k == 0) {
		return _pHead;
	}//根本不变

	struct SListNode* p1 = _pHead, * p2 = _pHead, * tail = _pHead, * rtn;
	int total = 0;
	//p1计数 p2导航 tail末尾指针 rtn输出
	while (tail->_PNext) {
		tail = tail->_PNext;
	}
	// 计数total
	while (p1) {
		total++;
		p1 = p1->_PNext;
	}
	k = k % total;
	if (k == 0) {
		return _pHead;
	}
	int move = total - k - 1;
	while (move--) {
		p2 = p2->_PNext;
	}
	rtn = p2->_PNext;			//rtn为新头
	p2->_PNext = NULL;			// p2作为新尾
	tail->_PNext = _pHead;		//将换了位置后重新链接
	return rtn;
}
void SListPrint2(struct SListNode* head) {
	while (head) {
		printf("%d--->", head->_data);
		head = head->_PNext;
	}
}//没有封装输出
void main() {
	SList s;

	SListInit(&s);
	SListPushBack(&s, 1);
	SListPushBack(&s, 2);
	SListPushBack(&s, 3);
	SListPrint(&s);
	SListPrint2(rotateRight(s._pHead, 4));

}