class Solution {
public:
	void replaceSpace(char *str,int length) {
		if (str==NULL || length < 0 )
            return;
        
        int originalLength = 0;
        int numberOfBlank = 0;
        int i = 0;
        while(str[i]!='\0'){
            originalLength++;
            if (str[i]==' ')
                numberOfBlank++;
            i++;
        }
        int newLength = originalLength + 2*numberOfBlank;
        if(newLength > length)
            return;
        int indexOfOriginal = originalLength;
        int indexOfNew = newLength;
        
        while(indexOfOriginal>=0 && indexOfOriginal <= indexOfNew  ){
            if(str[indexOfOriginal]==' '){
                str[indexOfNew--]='0';
                str[indexOfNew--]='2';
                str[indexOfNew--]='%';
            }else
                str[indexOfNew--]=str[indexOfOriginal];
            indexOfOriginal--;
        }
	}
};