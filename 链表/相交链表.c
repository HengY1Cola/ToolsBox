typedef int SDataType;
typedef struct SListNode
{
	SDataType _data;
	struct SListNode* _PNext;
};
struct SListNode*getIntersectionNode(SListNode* _PaNext,SListNode* _PbNext){
int count1=0,count2=0;
SListNode ret={0;NULL}
SListNode* p = _PaNext;
SListNode* q = _PbNext;//双指针
SListNode* headA=_PaNext;
SListNode* headB=_PbNext;//指路到头节点
while(p!=NULL){
p=p._PNext;
++count1;
}
while(q!=NULL){
q=q._PNext;
++count2;
}//计数
p=headA;
q=headB;//重新定到开头
while（p!=q）{
if(p==NULL){
p=headB;
}else{
p=p._PNext;
++ret._date;}
if(q==NULL){
q=headA;
}else
q=q._PNext;
if(ret._date>(count1+count2))
break;//判断没法相等
ret._PNext=p;}
return ret;