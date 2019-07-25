export PYTHONPATH := src:$(PYTHONPATH)

default: clean_derived #collate wrangle

# by default, we don't attempt to fetch new data

stash:
	./src/stash.py





# publish:
# 	./src/publish_viz.py

# ### CLEANING/DELETION STUFF
# clean: clean_derived


clean_all: clean_stashed clean_derived

clean_derived:
	rm -rf data/collated data/wrangled

clean_stashed:
	rm -rf data/stashed
