"""
Title     : Tuples
Subdomain : Data Types
Domain    : Python
Author    : Shubham Jirge
Created   : 18/12/2023
Problem   : https://www.hackerrank.com/challenges/python-tuples/problem
"""
if __name__ == "__main__":
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
