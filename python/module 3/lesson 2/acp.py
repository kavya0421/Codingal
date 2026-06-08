def shutdown(status):
    if status == "yes":
        print("Shutting down...")
    elif status == "no":
        print("Shutdown aborted")
    else:
        print("Sorry")

shutdown("yes")