

def main():
    i = 10
    print(i)
    import pdb;pdb.set_trace()
    i += 1
    print(i)


if __name__ == '__main__':
    # bt for backtrace
    # give variable name for state
    main()
