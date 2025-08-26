
class Cars{
public:
    Cars(int pos, int speed){

        this->pos = pos;
        this->speed = speed;
    }
    int pos;
    int speed;
};


class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {

        vector<Cars> cars;
        cars.reserve(position.size());

        for(int i = 0; i < position.size(); i++){
            cars.emplace_back(Cars(position[i], speed[i]));
        }

        //Lets sort the cars info based on position
        //So we have a sorted cars list based on position , along with other info
        sort(cars.begin(), cars.end(), [](const Cars &a, const Cars& b){
            return a.pos < b.pos;
        });

        //Monotonic decreasing stack
        //Speed increase violates monotonic property, also joins in a fleet
        stack<double>mq;
        double time_taken = (target - cars[0].pos) /(double) cars[0].speed;
        mq.push(time_taken);

        for(int i = 1; i < cars.size(); i++){
            double time_taken = (target - cars[i].pos) /(double) cars[i].speed;

            //Remember, its not only greater, its greater or equal
            //See Description: If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
            while(!mq.empty() && time_taken >= mq.top()){

                //We are using while loop because a new slower car might be blocking multiple
                // Early position faster cars
                // EG: 5->7->8->{6} : 6 blocks 8 & 7
                mq.pop();
            }

            mq.push(time_taken);
        }


        return mq.size();
    }
};