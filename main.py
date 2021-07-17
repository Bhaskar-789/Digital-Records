from dbhelper import DBHelper

def main():
    db=DBHelper()
    while True:
        print("******WELCOME******")
        print()
        print("Press 1 to insert new user")
        print("Press 2 to display  user")
        print("Press 3 to delete  user")
        print("Press 4 to update  user")
        print("Press 5 to exit program")
        print()
        try:
            choice=int(input())
            if choice==1:
                uid=int(input("enter userid"))
                username=input("enter username")
                userphone=input("enter userphone")
                db.insert_user(uid,username,userphone)
                pass
            elif choice==2:
                db.fetch_all()
                pass
            elif choice==3:
                userid=int(input("enter userid"))
                db.delete_user(userid)
                pass
            elif choice==4:
                uid=int(input("enter userid"))
                username=input("enter username")
                userphone=input("enter userphone")
                db.update_user(uid,username,userphone)
                pass
            elif choice==5:
                break
            else :
                print("Invalid Input")
        except Exception as e:
            print(e)
            print("Invalid details")

if __name__=="__main__":
    main()
