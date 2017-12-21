#include <iostream>

using namespace std;
//interface header file
class Base {
public:
    int n;
    Base(int n) : n(n) {}
    Base& operator=(Base& base);
};
//cpp file
Base& Base::operator=(Base& another){
    return another;
}


// interface header file
class ClaseCpp : public Base
{
public:
	ClaseCpp();
	
	/*
	if we comment on the two equals operator overloading, 
	the compilation process will give us a failure,
	the reason for this is that if we declare our destructor implementation,
	we must implement the copy operator and/or the move operator
	*/
    ~ClaseCpp();
	
	ClaseCpp(float, char, int);
	
	ClaseCpp(ClaseCpp& other);
	//test commenting on/off
	const ClaseCpp& operator=(const ClaseCpp& other){
	    cout <<"copy:"<<endl;
        return other;
	}
    //test commenting on/off
	const ClaseCpp& operator=(ClaseCpp&& other) noexcept{
	    cout <<"move:"<<endl;
        return other;
	}
	
	void printString();

private:
	const float mFloat;
    bool mBoolean;
	char mCharacter;
    int mInteger = 0;

};


//cpp file
ClaseCpp::ClaseCpp( float f, char a, int integer ) : Base(integer), mFloat( f ), mBoolean( true ) // option 1.
{
    // option 2
    mCharacter = a;
    mInteger = 0;
}



int main(int argc, char const *argv[])
{
	(void)argc;//just to avoid warning on linting
    (void)argv;//argc is the name of the executable created, 
    			//argv are the rest of the command line arguments
    ClaseCpp* cppHeap;
    ClaseCpp* cppStack2;
	ClaseCpp cppStack;

	{
	    
		cppHeap = new ClaseCpp(2.0f, 'a', 2);
		cout <<"paso0: "<<endl;
		ClaseCpp();

		cout <<"paso1: "<<endl;
		/*you ALWAYS SHOULD allocate in the stack because is faster. 
		But stack memory is SMALL 1MB, and can be runned out space 
		in a brief if you allocate too much objects in memory.
		arduino examples allocate the creation of objets this way because is faster(embedded systems) 
		as it's a requirement and all arduino memory is a stack, 
		cause it lacks of heap memory(wasnt designed with it in mind)
		*/ 
		cppStack = ClaseCpp();
		
		cout <<"paso2: "<<endl;
		ClaseCpp claseCpp;
		
		cout <<"paso3: "<<endl;
		claseCpp = ClaseCpp();
		
		cout <<"paso4: "<<endl;
		cppStack2 = &claseCpp;
		
		
		
		cout <<endl;
		cout <<"heap: "<< cppHeap<<endl;
		
		cout <<"stack: "<< &cppStack<<endl;
		
		cout <<"stack2: "<< cppStack2<<endl;
		cppStack2->printString();
		
		/*
		Deleting a pointer doesn't zero out any memory because to do so would take CPU cycles and that's not what C++ is about. 
		What you have there is a dangling pointer, and potentially a subtle error. Code like this can sometimes work for years 
		only to crash at some point in the future when some minor change is made somewhere else in the program.
        This is a good reason why you should NULL out pointers when you've deleted the memory they point to, 
        that way you'll get an immediate error if you try to dereference the pointer. 
        It's also sometimes a good idea to clear the memory pointed to using a function like memset(). 
        This is particularly true if the memory pointed to contains something confidential (e.g. a plaintext password) 
        which you don't want other, 
        possibly user facing, parts of your program from having access to.
        Cause you pay only for what you want
		*/
		//delete cppHeap;
		//cppHeap->printString();
		
		//this should fail cause it was destroyed already
		//delete cppStack2;
	}
	
	cout <<endl;
	cout<<"heap: "<<cppHeap<<endl;
	cout<<"stack: "<< &cppStack<<endl;
	//you pay only for what you want
	//la libreria SMFL esta creada de esta manera 
	cppStack.printString();
	cout <<"stack2: "<< cppStack2<<endl;
	
	//accesing to a dangling pointer
    cppStack2->printString();
    (*cppStack2).printString();
/*
	int* p;
	int i = 10;
	int& r = i; 
	p = &i;
	cout<<"pointer adress:"<<p<<endl;
	cout<<"pointer contain:"<<*p<<endl;
	cout<<"pointer contain:"<<r<<endl;


	p=0;
	p=NULL;
	p=nullptr;
	delete p;
*/


	return 0;
}

ClaseCpp::ClaseCpp():Base(3),mFloat(2.0){}
ClaseCpp::ClaseCpp(ClaseCpp& other):Base(3),mFloat(2.0){ }
ClaseCpp::~ClaseCpp(){cout << "destructing object in address: " << this << endl;}
void ClaseCpp::printString(){cout << "mensaje" << endl;}
