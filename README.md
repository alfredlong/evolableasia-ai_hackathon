# EVA Hackathon Development Environment


## Steps to install

1. Install Docker and Docker Compose

    Please install Docker Engine and Docker Compose at this [document](https://docs.docker.com/compose/install/).

    If you aren't familiar with Docker, please read the official documents.

2. Clone the repository

3. Build the image
    ```
    cd battleship-env
    docker-compose build
    ```

4. Test with the `random` bots

    `fig.sh` is just an alias of `docker-compose` command with an export `DOCKERHOST` variable.

    So please use this script instead of `docker-compose` to run the project.

    * Run
        ```
        ./fig.sh up -d
        ```

    * List the instances to confirm everything is working:
        ```
        ./fig.sh ps
        ```
    * Check logs
        ```
        ./fig.sh logs -f
        ./fig.sh logs -f bot1  # for bot1 only
        ```


4. Change the configuration to test your bot
    We already configured a random AI at `bot1` and `bot2`.
    
    To test your AI, just point `bot2`'s port to your running AI's port. 

    * Edit the file `bot_urls.txt`
        Default, the value `DOCKERHOST` is already understood by gamengine to point to your local host.
        
        So just change the port value if your AI running on another AI.
        
        Example: Your AI are running on `8080` port

        ```
        bot1,http://bot1:8000
        bot2,http://DOCKERHOST:8080
        ```
    
    * Use `local-bot.yml` instead of `docker-compose.yml`. 
        I already removed bot2 in `local-bot.yml`, so after editing the port in above step, just run:

        ```
        ./fig.sh -f local-bot.yml up -d
        ```
        
    > Summary: change `bot2` configuration in `bot_urls.txt` to your AI (id, name)
     
5. Access to `http://localhost/bb` to try it

## Some docker/docker-compose commands

> Note that, to running our project, please run `fig.sh` instead of `docker-compose`.

```
docker-compose build
docker-compose up
docker-compose up gameengine  # to run up gameengine
docker-compose up -d  # to run in background
docker-compose logs -f
docker-compose logs -f bot1
docker-compose stop
docker-compose start
docker-compose down
```
