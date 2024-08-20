from vehicule import vehicule

def main():
    my_car = vehicule("Ford", "Explorer", 4)
    my_car.run()
    my_car.door_open()
    my_car.stop()
    
if __name__ == "__main__":
    main()