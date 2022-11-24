FROM ubuntu:20.04
RUN apt-get -y update
# update and install dependencies
RUN  apt-get update \
    && apt-get install -y \
<<<<<<< Updated upstream
    make \
    git \
=======
        make \
        git \
>>>>>>> Stashed changes
    && apt install -y build-essential
RUN apt-get purge mysql*
RUN apt-get clean
RUN apt-get autoremove
RUN apt-get autoclean
RUN apt-get update
RUN apt-get install -y sqlite3 libsqlite3-dev
RUN apt-get install -y python3-mysqldb
RUN apt-get install -y python3-pip
<<<<<<< Updated upstream
RUN pip3 install flask SQLAlchemy
=======
RUN pip3 install flask SQLAlchemy
>>>>>>> Stashed changes
