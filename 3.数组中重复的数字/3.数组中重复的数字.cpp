class Solution {
public:
    // Parameters:
    //        numbers:     an array of integers
    //        length:      the length of array numbers
    //        duplication: (Output) the duplicated number in the array number
    // Return value:       true if the input is valid, and there are some duplications in the array number
    //                     otherwise false
    bool duplicate(int numbers[], int length, int* duplication) {
        for(int i=0;i<length;i++){
            int val = numbers[i];
            if(i!=val){//避免第一次相等的判断
                if (numbers[numbers[i]]==val){
                *duplication = val;
                return true;
                }
            }
            numbers[i] = numbers[val];
            numbers[val] = val;
        }
        *duplication = -1;
        return false;
    }
};
