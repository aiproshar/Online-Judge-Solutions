class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int>st;



        int ans = 0;

        for(const auto& it: tokens){
            if(it == "+" ||it == "-" || it == "*" || it == "/"  ){
                auto num_2 = st.top(); st.pop();
                auto num_1 = st.top(); st.pop();

                if(it == "+"){
                    auto eval = num_1 + num_2;
                    st.push(eval);
                }
                if(it == "-"){
                    auto eval = num_1 - num_2;
                    st.push(eval);
                }
                if(it == "*"){
                    auto eval = num_1 * num_2;
                    st.push(eval);
                }
                if(it == "/"){
                    auto eval = num_1 / num_2;
                    st.push(eval);
                }

            }else{
                st.push(stoi(it));
            }
        }
        return st.top();
    }
};