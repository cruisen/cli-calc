#! /bin/ksh

cd $(git rev-parse --show-toplevel)

git status
echo ""

if (( $? -ne 0 )) ; then
  cd -
  echo "Exiting..."
  exit
fi


if [[ $(git status --porcelain) ]] ; then
  cd -
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

if (( $? -eq 0 )) ; then
  poetry version patch

  gh release create "v$(poetry version --short)" --generate-notes

  git add .
  git commit -m "Update to $(poetry version --short)."
  git push --tags
  git push
  echo ""
else
  cd -
  echo"poetry build error. Exiting..."
  exit
fi

if [[ $1 == "publish" ]] ; then
  poetry publish --build
fi

cd -

