{ pkgs ? import <nixpkgs> {} }:
	let lexique = pkgs.stdenv.mkDerivation rec {
        name = "${pname}-${version}.tsv";
		pname = "lexique";
		version = "383";
		src = pkgs.fetchzip {
			url = "http://www.lexique.org/databases/Lexique${version}/Lexique${version}.zip";
			sha256 = "t9zWZhyFc9DAPIHP3f14eik1e3W+k9hzCwnbJNEmQTY=";
			stripRoot = false;
		};
		installPhase = ''
            cp Lexique${lexique.version}.tsv $out
		'';
	};
	in
	pkgs.mkShell {
		buildInputs = [
			pkgs.python310Packages.pandas
		];
		shellHook = ''
			export LEXIQUE_TSV=${lexique}
		'';
}
