class Solution {
public:
    void reOrderArray(vector<int> &array) {
        for(int i=0;i<array.size();i++){
            for(int j = 0;j<array.size()-1-i;j++){
                if (array[j]%2 == 0 && array[j+1]%2==1){
                    swap(array[j],array[j+1]);
                }
            }
        }
    }
};