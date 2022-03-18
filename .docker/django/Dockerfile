FROM python:3.8-slim as base

RUN adduser --disabled-password --disabled-login sc_forum
USER sc_forum

WORKDIR /home/sc_forum/app

ENV PATH="/home/sc_forum/.local/bin:${PATH}"

COPY --chown=sc_forum:sc_forum requirements.txt requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --user -r requirements.txt

COPY --chown=sc_forum:sc_forum . /home/sc_forum/app/
