#!/usr/bin/env python3

# Created by: Melody Berhane
# Created on: Jan. 17, 2022
# This program prints numbers from 1000 to 2000.

def main():
    # this function is the the famous Fizz-Buzz problem

    for counter in range(1000, 2001, 1):
        if counter % 5 == 0:
            print()
        print(counter, " ", end="")


if __name__ == "__main__":
    main()
