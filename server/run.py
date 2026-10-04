from app import create_app

nala_server = create_app()
if __name__ == "__main__":
    print("starting server...")
    nala_server.run(debug=True)
