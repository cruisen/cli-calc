#! /bin/ksh

git status
echo ""
if [[ $? -ne 0 ]] ; then
  echo "Exiting..."
  exit
fi

cd $(git rev-parse --show-toplevel)

if [[ $(git status --porcelain) ]] ; then
  echo ""
  echo "Exiting..."
  echo "Clean up before trying again."
  exit
fi

echo "git pull:"
git pull
echo ""

poetry build
echo ""

if [[ $? -eq 0 ]] ; then
  poetry version patch

  gh release create "v$(poetry version --short)" --generate-notes

  git add .
  git commit -m "Update to $(poetry version --short)."
  git push --tags
  git push
  echo ""
else
  echo"poetry build error. Exiting..."
  exit
fi

if [[ $1 == "publish" ]] ; then
  poetry publish --build
fi

