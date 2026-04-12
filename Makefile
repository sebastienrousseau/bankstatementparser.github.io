.PHONY: build serve clean

LOCALES := en fr de es it pt nl pl ro sv cs ar bn ha he hi id ja ko ru th tl tr uk vi yo zh zh-tw

build:
	@echo "Building all 28 locales..."
	@for locale in $(LOCALES); do \
	  layout_dir=_layouts/$$locale; \
	  post_dir=_posts/$$locale; \
	  if [ "$$locale" = "en" ]; then prefix=""; else prefix="$$locale/"; fi; \
	  count=0; \
	  for f in $$post_dir/*.md; do \
	    name=$$(basename $$f .md); \
	    rm -rf /tmp/bsp_build /tmp/bsp_build.build-tmp /tmp/bsp_out /tmp/bsp_out.build-tmp; \
	    mkdir -p /tmp/bsp_build; cp $$f /tmp/bsp_build/; \
	    ssg -c /tmp/bsp_build -o /tmp/bsp_out -t $$layout_dir 2>/dev/null; \
	    if [ "$$name" = "index" ]; then src=/tmp/bsp_out.build-tmp/index.html; else src=/tmp/bsp_out.build-tmp/$$name/index.html; fi; \
	    dst=docs/$${prefix}$${name}/index.html; \
	    [ "$$name" = "index" ] && dst=docs/$${prefix}index.html; \
	    if [ -f "$$src" ]; then mkdir -p $$(dirname $$dst); cp $$src $$dst; count=$$((count+1)); fi; \
	  done; \
	  rm -rf /tmp/bsp_build /tmp/bsp_build.build-tmp /tmp/bsp_out /tmp/bsp_out.build-tmp; \
	  echo "$$locale: $$count pages"; \
	done
	@echo "Done."

serve: build
	@echo "Serving at http://127.0.0.1:8000"
	@python3 -m http.server --directory docs 8000

clean:
	@rm -rf /tmp/bsp_build /tmp/bsp_build.build-tmp /tmp/bsp_out /tmp/bsp_out.build-tmp public public.build-tmp
