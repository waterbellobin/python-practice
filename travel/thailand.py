class ThailandTravel:
    def detail(self):
        print("Thailand")

if __name__ == "__main__":
    print("Thailand module runs directly")
    trip = ThailandTravel()
    trip.detail()
else:
    print("out of Thailand")