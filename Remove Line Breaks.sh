#!/bin/bash

pbpaste | tr -d '\r' | tr '\n' ' ' | pbcopy