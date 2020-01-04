class Solution {
public:
    void reOrderArray(vector<int> &array) {
        for(int i = 0 ;i<array.size();i++){
            int key = array[i];
            if (key%2==0){
                continue;
            }
            int j = i - 1;
            while(j>=0 and array[j]%2==0){
                array[j+1] = array[j];
                    j = j - 1;
            }
            array[j+1] = key;
        }
    }
};